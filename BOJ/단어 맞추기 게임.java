import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class HangmanGame {

    public static void main(String[] args) {
        List<String> cards = new ArrayList<>();
        cards.add("PICTURE");
        cards.add("APPLE");
        cards.add("HELLO");
        cards.add("EXPENSIVE");

        Random random = new Random();
        int randNumber = random.nextInt(cards.size());
        String answer = cards.get(randNumber);

        // prompt를 char 리스트로 바꿔서 한글자씩 "_"를 저장
        List<Character> prompt = new ArrayList<>();
        for (int i = 0; i < answer.length(); i++) {
            prompt.add('_');  // 각 자리에 '_' 문자 추가
        }

        List<Character> save = new ArrayList<>();  // 이미 입력된 알파벳을 저장

        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 9; i++) {  // 최대 9번까지 시도
            while (true) {
                // 현재 상태의 단어 출력
                for (char c : prompt) {
                    System.out.print(c + " ");
                }
                System.out.println();

                // 사용자 입력
                String value = scanner.nextLine().toUpperCase();  // 대문자 입력 받기
                if (value.length() == 1 && value.charAt(0) >= 'A' && value.charAt(0) <= 'Z' && !save.contains(value.charAt(0))) {
                    save.add(value.charAt(0));  // 입력한 알파벳 저장
                    break;
                } else {
                    System.out.println("유효하지 않은 입력입니다. 다시 시도하세요.");
                }
            }

            // prompt 업데이트
            char alpabet = save.get(save.size() - 1);  // 마지막으로 입력된 알파벳
            for (int j = 0; j < answer.length(); j++) {
                if (alpabet == answer.charAt(j)) {
                    prompt.set(j, alpabet);  // 맞는 알파벳을 prompt에 업데이트
                }
            }

            // 승리 조건 체크
            if (!prompt.contains('_')) {
                System.out.println("승리!");
                break;
            }
        }

        // 게임 종료 후 최종 상태 출력
        for (char c : prompt) {
            System.out.print(c + " ");
        }
        System.out.println();
    }
}
