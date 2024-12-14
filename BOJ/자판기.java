import java.util.Scanner;

public class 스파르타자판기 {
    public static void main(String[] args) {

        //Scanner 객체 생성
        Scanner scanner = new Scanner(System.in);

        System.out.println("사이다 1,700원");
        System.out.println("콜라 1,900원");
        System.out.println("식혜 2,500원");
        System.out.println("솔의눈 3,000원");

        String name = scanner.nextLine();

        //목록에 없는 음료일 경우 실행 종료
        if (!name.equals("사이다") && !name.equals("콜라") && !name.equals("식혜") && !name.equals("솔의눈")) {
            System.exit(0);
        }

        Integer money = scanner.nextInt();

        if (name.equals("사이다")) {
            if (money < 1700) {
                System.out.println("돈이 부족합니다");
            } else {
                System.out.println(money - 1700);
            }
        }

        if (name.equals("콜라")) {
            if (money < 1900) {
                System.out.println("돈이 부족합니다");
            } else {
                System.out.println(money - 1900);
            }
        }

        if (name.equals("식혜")) {
            if (money < 2500) {
                System.out.println("돈이 부족합니다");
            } else {
                System.out.println(money - 2500);
            }
        }

        if (name.equals("솔의눈")) {
            if (money < 3000) {
                System.out.println("돈이 부족합니다");
            } else {
                System.out.println(money - 3000);
            }
        }

    }
}
