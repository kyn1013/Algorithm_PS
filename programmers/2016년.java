import java.util.Calendar;
import java.util.Scanner;

public class DayOfWeekFinder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 사용자 입력 받기
        System.out.print("월을 입력하세요 (1-12): ");
        int month = scanner.nextInt();

        System.out.print("날짜를 입력하세요 (1-31): ");
        int day = scanner.nextInt();

        // 2016년을 기준으로 Calendar 객체 생성 (month는 0부터 시작하므로 -1 필요)
        Calendar calendar = Calendar.getInstance();
        calendar.set(2016, month - 1, day);

        // 요일 구하기
        int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);
        String[] weekDays = {"일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"};

        // 결과 출력
        System.out.println("2016년 " + month + "월 " + day + "일은 " + weekDays[dayOfWeek - 1] + "입니다.");

        scanner.close();
    }
}