using System;
using System.Threading;
using System.Threading.Channels;
using System.Threading.Tasks;

namespace Programma
{
    class Creater
    {
        private ChannelWriter<int> Writer;
        public Creater(ChannelWriter<int> _writer, CancellationToken tunnel)
        {
            Writer = _writer;
            Task.WaitAll(Run(tunnel));
        }

        private async Task Run(CancellationToken tunnel)
        {
            var r = new Random();
            //ожидает, когда освободиться место для записи элемента.
            while (await Writer.WaitToWriteAsync())
            {
                if (tunnel.IsCancellationRequested)
                {
                    Console.WriteLine("Производство остановлено.");
                    return;
                }
                if (Program.tumbler && Program.count <= 100)
                {
                    var product = r.Next(1, 101);
                    await Writer.WriteAsync(product);
                    Program.count += 1;
                    Console.WriteLine($"Записанные данные: {product}");
                }
            }
        }
    }

    class Buyer
    {
        private ChannelReader<int> Reader;

        public Buyer(ChannelReader<int> _reader, CancellationToken tunnel)
        {
            Reader = _reader;
            Task.WaitAll(Run(tunnel));
        }

        private async Task Run(CancellationToken tunnel)
        {
            // ожидает, когда освободиться место для чтения элемента.
            while (await Reader.WaitToReadAsync())
            {
                if (Reader.Count != 0)
                {
                    var product = await Reader.ReadAsync();
                    Program.count -= 1;
                    Console.WriteLine($"\tПолученные данные: {product}");
                }
                if (Reader.Count >= 100)
                {
                    Program.tumbler = false;
                }
                else if (Reader.Count <= 80)
                {
                    Program.tumbler = true;
                }
                //проверка токена
                if (tunnel.IsCancellationRequested)
                {
                    if (Reader.Count == 0)
                    {
                        Console.WriteLine("\t Потребление остановлено. ");
                        return;
                    }
                }
            }
        }
    }

    class Program
    {
        static public bool tumbler = true;
        static public int count = 0;

        static void printMenu()
        {

            bool tumbler = true;
            while (tumbler)
            {
                Console.WriteLine("#### МЕНЮ ПРОГРАММЫ КОНВЕЕР ####");
                Console.WriteLine("## 1. Запустить задание.");
                Console.WriteLine("## 0. Выйти из программы.");
                Console.Write("## Выберите пункт меню: ");
                int num = int.Parse(Console.ReadLine());
                switch (num)
                {
                    case 1:
                        //создаю общий канал данных
                        Channel<int> channel = Channel.CreateBounded<int>(200);
                        //создал токен отмены
                        var cts = new CancellationTokenSource();
                        //создаются производители и потребители
                        Task[] streams = new Task[5];
                        for (int i = 0; i < 5; i++)
                        {
                            if (i < 3)
                            {
                                streams[i] = Task.Run(() => { new Creater(channel.Writer, cts.Token); }, cts.Token);
                            }
                            else
                            {
                                streams[i] = Task.Run(() => { new Buyer(channel.Reader, cts.Token); }, cts.Token);
                            }
                        }
                        //Создается поток проверки нажатия клавиши
                        new Thread(() =>
                        {
                            for (; ; )
                            {
                                if (Console.ReadKey(true).Key == ConsoleKey.Q)
                                {
                                    cts.Cancel();
                                }
                            }
                        })
                        { IsBackground = true }.Start();
                        //Ожидает завершения выполнения всех указанных объектов Task 
                        Task.WaitAll(streams);
                        break;

                    case 0:
                        tumbler = false;
                        break;

                    default:
                        Console.WriteLine("Пункт меню не существует");
                        break;
                }
            }
        }

        static void Main(string[] args)
        {
            printMenu();
        }
    }
}
