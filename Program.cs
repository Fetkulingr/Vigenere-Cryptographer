namespace Vigenere_Cryptographer
{

    class Program
    {
        enum EncryptionType { Encode, Decode }
        // Массив русского алфавита    
        const string alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";

        static void Main()
        {
            while (true)
            {
                // Вывод текста на экран и настройка управления 
                Console.Clear();
                Console.WriteLine("Шифр Виженера, версия 1.0");
                Console.WriteLine("Copyright 2022 Феткулин Григорий");
                Console.WriteLine("Что нужно делать?");
                Console.WriteLine("Ш - Шифровать текст.");
                Console.WriteLine("Р - Расшифровать текст.");
                Console.WriteLine("ESC - Закрыть программу.");
                switch (Console.ReadKey(true).Key)
                {
                    case ConsoleKey.D1:
                    case ConsoleKey.I:
                        MainVigener(EncryptionType.Encode);
                        break;
                    case ConsoleKey.D2:
                    case ConsoleKey.H:
                        MainVigener(EncryptionType.Decode);
                        break;
                    case ConsoleKey.Escape:
                        return;
                }
            }
        }

        //Метод взаимодествия
        static void MainVigener(EncryptionType encryptionType)
        {
            // Проверка ключа на наличие пустой строки и на совпадение с массивом русского алфавита.
            static bool CheckKeyString(string key)
                => !string.IsNullOrWhiteSpace(key) && key.All(symbol => alf.Contains(symbol));

            //Получение информации для шифрования / расшифрования текста
            Console.Clear();
            Console.Write("Введите текст: ");
            string text = Console.ReadLine();
            Console.Write("Введите ключ: ");
            string key = Console.ReadLine();

            //Вывод полученных данных
            Console.Write("Результат: ");
            Console.WriteLine(CheckKeyString(key)
                ? "\r\n" + VigenerEncryption(text, key, encryptionType)
                : "\r\nКлюч введен некорректно !");
            Console.WriteLine("\r\nНажмите любую клавишу для выхода...");
            Console.ReadKey(true);
        }

        // Метод шифрования / расшифрования
        static string VigenerEncryption(string text, string key, EncryptionType encryptionType)
        {
            // Индекс текущего символа ключа
            int keyIndex = -1;
            // Получение следующего символа ключа
            char NextKeySymbol()
            => key[++keyIndex < key.Length ? keyIndex : keyIndex = 0];
            // Шифрование символа: (t + k) % aLen
            char EncryptSymbol(char symbol)
            => alf[(alf.IndexOf(symbol) + alf.IndexOf(NextKeySymbol())) % alf.Length];
            // Расшифрование символа: (t + aLen - k) % aLen
            char DecryptSymbol(char symbol)
            => alf[(alf.IndexOf(symbol) + alf.Length - alf.IndexOf(NextKeySymbol())) % alf.Length];

            //  Выполнение процедуры шифрования/дешифрования для символов входящих в массив алфавита
            return encryptionType switch
            {
                EncryptionType.Encode => new string(text.Select(s => alf.Contains(s) ? EncryptSymbol(s) : s).ToArray()),
                EncryptionType.Decode => new string(text.Select(s => alf.Contains(s) ? DecryptSymbol(s) : s).ToArray()),
                _ => "",
            };
        }
    }
}