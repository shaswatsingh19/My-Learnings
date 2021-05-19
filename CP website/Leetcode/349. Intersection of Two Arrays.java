class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet<>();
        Set<Integer> s2 = new HashSet<>();
        for(int i:nums1) s1.add(i);        for(int i:nums2) s2.add(i);
        System.out.println(s1);        System.out.println(s2);
        s1.retainAll(s2);
                System.out.println(s1);
        int [] arr = new int[s1.size()];
        int i=0;
        for(int s: s1){
            arr[i++] = s; 
        }
        return arr;
    }
}