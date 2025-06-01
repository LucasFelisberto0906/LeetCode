class Solution {
    public static boolean isPalindrome(String s) {
        StringBuilder formatada = new StringBuilder();

        for(char c : s.toCharArray()) {
            if(Character.isLetterOrDigit(c)) {
                formatada.append(Character.toLowerCase(c));
            }
        }
        
        return formatada.toString().equals(formatada.reverse().toString());
    }
}