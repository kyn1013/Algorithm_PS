import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class 랜덤닉네임생성기 {
    public static void main(String[] args) {
        List<String> list1 = new ArrayList<>();
        list1.add("기절초풍");
        list1.add("멋있는");
        list1.add("재미있는");

        List<String> list2 = new ArrayList<>();
        list2.add("도전적인");
        list2.add("노란색의");
        list2.add("바보같은");

        List<String> list3 = new ArrayList<>();
        list3.add("돌고래");
        list3.add("개발자");
        list3.add("오랑우탄");

        List<String> nameList = new ArrayList<>();

        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                for (int k = 0; k < 3; k++){
                    String nickName = list1.get(i) + " " +list2.get(j) + " " + list3.get(k);
                    nameList.add(nickName);
                }
            }
        }

        Random random = new Random();
        int randNumber = random.nextInt(28);

        System.out.print(nameList.get(randNumber));
    }
}
