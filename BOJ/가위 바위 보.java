import java.util.*;

public class 가위바위보 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        List<String> words = Arrays.asList("가위", "바위", "보");
        int winCount = 0;

        for (int i = 0; i < 5; i++){
            String user = scanner.nextLine();
            if (!user.equals("가위") && !user.equals("바위") && !user.equals("보")){
                System.out.println("잘못된 입력입니다.");
            }

            String computer = words.get(random.nextInt(words.size()));

            switch (user) {
                case "가위":
                    if (computer.equals("보")){
                        winCount++;
                        System.out.println("승리");
                    } else {
                        System.out.println("패배");
                    }
                    break;

                case "바위":
                    if (computer.equals("가위")){
                        winCount++;
                        System.out.println("승리");
                    } else {
                        System.out.println("패배");
                    }
                    break;

                case "보":
                    if (computer.equals("바위")){
                        winCount++;
                        System.out.println("승리");
                    } else {
                        System.out.println("패배");
                    }
                    break;
            }

        }

        Map<Integer, String> gifts = new HashMap<>();
        gifts.put(0, "꽝");
        gifts.put(1, "초코비인형");
        gifts.put(2, "부리부리맨인형");
        gifts.put(3, "흰둥이인형");
        gifts.put(4, "짱아인형");
        gifts.put(5, "짱구인형");

        System.out.println("총 " + winCount + "회 승리하여 [" + gifts.get(winCount) + "]를 경품으로 획득!");
    }
}
