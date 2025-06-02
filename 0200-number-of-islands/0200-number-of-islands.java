class Solution {
    static int MAX = 300;
    static boolean[][] visited;
    static int r, c;

    // x -> linhas r, y -> colunas, c
	public static void dfs(int x, int y, char[][] grid) {
		if(x<0 || x>= r || y<0 || y>=c ) { return;}
		if(visited[x][y] ||  grid[x][y] != '1') { return;}
		visited[x][y] = true;
		dfs(x,y-1, grid); // esquerda
		dfs(x,y+1, grid); // direita
		dfs(x-1,y, grid); // cima
		dfs(x+1,y, grid); // baixo
	}
    public int numIslands(char[][] grid) {

        r = grid.length;
        c = grid[0].length;
        visited = new boolean[r][c];

        int contador = 0;
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[i].length; j++) {
                if(!visited[i][j] && grid[i][j] == '1'){
                	contador++;
                	dfs(i, j, grid);
                }
            }
        }
        return contador;
    }
}