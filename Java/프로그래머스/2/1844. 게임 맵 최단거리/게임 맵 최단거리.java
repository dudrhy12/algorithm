import java.util.*;

class Solution {
    int answer = 0;
    // 동서남북 순서
    int[] dx = {+1, -1, 0, 0};
    int[] dy = {0, 0, +1, -1};
    int currentX = 0;
    int currentY = 0;
    public int solution(int[][] maps) {
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{currentX, currentY});
        
        int[][] distance = new int[maps.length][maps[0].length];
        distance[0][0] = 1;
        
        maps[currentX][currentY] = 0;
        
        while (!queue.isEmpty()){
            int[] current = queue.poll();
            
            currentX = current[0];
            currentY = current[1];
            
            if (currentX == maps.length -1 && currentY == maps[0].length-1){
                return distance[currentX][currentY];
            }
            
            for (int i=0; i<4; i++){
                int nextX = currentX + dx[i];
                int nextY = currentY + dy[i];
                
                if (nextX < 0 || nextY < 0 || nextX >= maps.length || nextY >= maps[0].length){
                    continue;
                }
                
                if (maps[nextX][nextY] != 1){
                    continue;
                }
                
                maps[nextX][nextY] = 0;
                distance[nextX][nextY] = distance[currentX][currentY] +1;
                queue.offer(new int[]{nextX, nextY});
                answer ++;
            }
            
        }

        return -1;
    }
    

}