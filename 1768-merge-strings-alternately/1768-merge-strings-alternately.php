class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return String
     */
    function mergeAlternately($word1, $word2) {
        $rs="";
        $s1=$word1;
        $s2=$word2;
        $l1=strlen($s1);
        $l2=strlen($s2);
        $min=max($l1,$l2);
        for($i=0;$i<$min;$i++){
            if($i<$l1)
                $rs.=$word1[$i];
            if($i<$l2)
                $rs.=$word2[$i];
        }
        // $diff=$l1-$l2;
        // if($diff<0){
        //     for($i=$min;$i<$l2;$i++){
        //         $rs.=$word2[$i];
        //     }
        // }
        // else{
        //     for($i=$min;$i<$l1;$i++){
        //         $rs.=$word1[$i];
        //     }
        // }
        return $rs;
    }
}