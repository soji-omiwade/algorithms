class Solution {
   public boolean isSubsequence(String s, String t) {
        List<Integer>[] idx = new List[256]; // Just for clarity
        for (int i = 0; i < s.length(); i++) {
            idx[s.charAt(i)] = new ArrayList<>();
        }
        for (int i = 0; i < t.length(); i++) {
            if (idx[t.charAt(i)] == null)
                idx[t.charAt(i)] = new ArrayList<>();
            idx[t.charAt(i)].add(i);
        }
        int prev = 0;
        for (int i = 0; i < s.length(); i++) {
            //if (idx[s.charAt(i)] == null) return false; // Note: char of S does NOT exist in T causing NPE
            prev = Collections.binarySearch(idx[s.charAt(i)], prev);
            if (prev < 0) {
                prev = -(prev + 1);
            }
            if (prev == idx[s.charAt(i)].size()) 
                return false;
            prev = idx[s.charAt(i)].get(prev) + 1;
        }
        return true;
    }
}
/*
   public boolean isSubsequence(String s, String t) {
        List<Integer>[] idx = new List[256]; // Just for clarity
        for (int i = 0; i < t.length(); i++) {
            if (idx[t.charAt(i)] == null)
                idx[t.charAt(i)] = new ArrayList<>();
            idx[t.charAt(i)].add(i);
        }
        
        int prev = 0;
        for (int i = 0; i < s.length(); i++) {
            if (idx[s.charAt(i)] == null) return false; // Note: char of S does NOT exist in T causing NPE
            int j = Collections.binarySearch(idx[s.charAt(i)], prev);
            if (j < 0) j = -j - 1;
            if (j == idx[s.charAt(i)].size()) return false;
            prev = idx[s.charAt(i)].get(j) + 1;
        }
        return true;
    }
*/
