import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = 100;
        int aSide = 0;
        int aCount = 0;
        int bCount = 0;
        
        for (int i=0; i< wires.length; i++){
            aSide = wires[i][0];
            Set<Integer> aSideWires = new HashSet<>();
            aSideWires.add(aSide);

            boolean added = true;

            while (added) {
                added = false;

                for (int j = 0; j < wires.length; j++) {
                    if (j == i) {
                        continue;
                    }

                    int a = wires[j][0];
                    int b = wires[j][1];

                    if (aSideWires.contains(a) && !aSideWires.contains(b)) {
                        aSideWires.add(b);
                        added = true;
                    } else if (aSideWires.contains(b) && !aSideWires.contains(a)) {
                        aSideWires.add(a);
                        added = true;
                    }
                }
            }

            aCount = aSideWires.size();
            bCount = n - aCount;

            answer = Math.min(answer, Math.abs(aCount - bCount));
        }

        return answer;
    }
}