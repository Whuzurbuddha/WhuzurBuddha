using System.Security.Cryptography;
using System.Windows;

namespace PasswordGenerator;

/// <summary>
/// Interaction logic for MainWindow.xaml
/// </summary>
public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }
    [Obsolete("Obsolete")]
    private void GeneratePassword(object sender, RoutedEventArgs gp)
    {
        var length = (int)Slider.Value;
        Console.Write(length);
        const string validChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:'\",.<>?";
        var password = new char[length];

        using (var rng = new RNGCryptoServiceProvider())
        {
            var validCharCount = validChars.Length;
            var randomNumber = new byte[1];

            for (var i = 0; i < length; i++)
            {
                do
                {
                    rng.GetBytes(randomNumber);
                } while (randomNumber[0] >= validCharCount * (Byte.MaxValue / validCharCount));

                var randomCharIndex = randomNumber[0] % validCharCount;

                password[i] = validChars[randomCharIndex];
            }
        }

        var newPassword = new string(password);
        NewPassword.Text = newPassword;
        Clipboard.SetText(newPassword);
        Info.Visibility = Visibility.Visible;
    }
}
