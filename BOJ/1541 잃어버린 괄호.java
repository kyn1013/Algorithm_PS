import java.util.Scanner;

public class 잃어버린괄호 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        String[] parts = input.split("-");
        int result = Integer.parseInt(parts[0]);

        for (int i = 1; i < parts.length; i++){
            result -= sum(parts[i]);
        }

        System.out.print(result);
    }

    public static int sum(String str){
        //String을 담을 수 있는 배열
        String[] numbers = str.split("\\+");
        int sum = 0;
        for (String number : numbers){
            sum += Integer.parseInt(number);
        }

        return sum;
    }
}
