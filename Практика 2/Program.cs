using System;
using System.IO;
using System.Diagnostics;
using System.Threading.Channels;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Os_Lab_2
{
    public class Jdi
    {
        private ChannelWriter<string> type;
        public Jdi(ChannelWriter<string> channel)
        {
            type = channel;
            Task.WaitAll(Run());
        }

        private async Task Run()
        {
            while (await type.WaitToWriteAsync())
            {
                char[] text = new char[5];
                for (int i = 97; i < 123; i++)
                {
                    text[0] = (char)i;
                    for (int j = 97; j < 123; j++)
                    {
                        text[1] = (char)j;
                        for (int g = 97; g < 123; g++)
                        {
                            text[2] = (char)g;
                            for (int q = 97; q < 123; q++)
                            {
                                text[3] = (char)q;
                                for (int s = 97; s < 123; s++)
                                {
                                    text[4] = (char)s;
                                    if (Program.toggle is true)
                                    {
                                        await type.WriteAsync(new string(text));
                                    }
                                    else
                                    {
                                        return;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    public class unhas
    {
        private ChannelReader<string> reader;
        private string passhash;
        public unhas(ChannelReader<string> readers, string passhashs)
        {
            reader = readers;
            passhash = passhashs;

            Task.WaitAll(Run());
        }
        private async Task Run()
        {
            while (await reader.WaitToReadAsync())
            {
                if (Program.toggle is true)
                {

                    var pass = await reader.ReadAsync();
                    if (hashs(pass.ToString()) == passhash)
                    {
                        Console.WriteLine($"Пароль успешно найден - {pass}");
                        Program.toggle = false;

                    }
                }
                else
                {
                    return;
                }
            }
        }

        static public string hashs(string str)
        {
            SHA256 sha256 = SHA256.Create();
            byte[] bytes = Encoding.ASCII.GetBytes(str);
            byte[] hashBytes = sha256.ComputeHash(bytes);
            string stroka = BitConverter.ToString(hashBytes).Replace("-", String.Empty);
            stroka = stroka.ToLower();
            return stroka;
        }

    }

    public class Program
    {
        static public bool toggle = true;
        static void Menu()
        {

            while (toggle is true)
            {
                Console.WriteLine("------МЕНЮ ПРОГРАММЫ------");
                Console.WriteLine("| 1. Запуск подбора.");
                Console.WriteLine("| 2. Закрыть программу.");
                Console.Write("| Введите номер пункта: ");

                int target = int.Parse(Console.ReadLine());
                switch (target)
                {
                    case 1:
                        Console.WriteLine("------МЕНЮ ПРОГРАММЫ --> Запуск подбора------");
                        Console.Write("Укажите число потоков: ");
                        int potok = int.Parse(Console.ReadLine());
                        Console.WriteLine("Выберите хэш значение: ");
                        Console.WriteLine("1. 1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad");
                        Console.WriteLine("2. 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b");
                        Console.WriteLine("3. 74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f");
                        Console.WriteLine("4. bbbf7a6412d6d3e8244ac1fda5e35a20037acee661288cb95b7b18cf469980aa");
                    back:
                        Console.Write("Введите номер пункта: ");
                        int hash_point = int.Parse(Console.ReadLine());

                        string hash = "";
                        if (hash_point == 1)
                        {
                            hash = "1115DD800FEAACEFDF481F1F9070374A2A81E27880F187396DB67958B207CBAD";
                        }
                        else if (hash_point == 2)
                        {
                            hash = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b";
                        }
                        else if (hash_point == 3)
                        {
                            hash = "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f";
                        }
                        else if(hash_point == 4)
                        {
                            hash = "bbbf7a6412d6d3e8244ac1fda5e35a20037acee661288cb95b7b18cf469980aa"; //brain
                        
                        }
                        else
                        {
                            Console.WriteLine("Того номера нет. Введите снова!");
                            goto back;
                        }

                        Console.WriteLine("Функция подбора запущена!");
                        Stopwatch timer = new Stopwatch();
                        timer.Reset();
                        timer.Start();

                        Channel<string> channel = Channel.CreateBounded<string>(potok);
                        var a = Task.Run(() => { new Jdi(channel); });

                        Task[] potoks = new Task[potok + 1];
                        potoks[0] = a;

                        Console.WriteLine("------Отчет------");
                        for (int i = 0; i < potok + 1; i++)
                        {
                            potoks[i] = Task.Run(() => { new unhas(channel.Reader, hash); });
                        }
                        Task.WaitAny(potoks);
                        timer.Stop();
                        Console.WriteLine($"Затраченное время на подбор: {timer.Elapsed}");
                        toggle = true;
                        break;

                    case 2:
                        toggle = false;
                        break;

                    default:
                        Console.WriteLine("Ошибка. Таккого номера пункта нет");
                        break;
                }
            }
        }
        static public void Main(string[] args)
        {
            Menu();
        }
    }
}
