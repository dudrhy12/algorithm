class Solution {
    public int solution(String name) {
        int answer = 0;

        // 알파벳 변경 횟수
        for (int i = 0; i < name.length(); i++) {
            answer += Math.min(
                up('A', name.charAt(i)),
                down('A', name.charAt(i))
            );
        }

        // 좌우 이동 횟수
        int move = name.length() - 1;

        for (int i = 0; i < name.length(); i++) {
            int next = i + 1;

            while (next < name.length() && name.charAt(next) == 'A') {
                next++;
            }

            move = Math.min(move, i * 2 + name.length() - next);
            move = Math.min(move, (name.length() - next) * 2 + i);
        }

        return answer + move;
    }

    public int up(char c, char target) {
        return (target - c + 26) % 26;
    }

    public int down(char c, char target) {
        return (c - target + 26) % 26;
    }
}