class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $arr = array();
        for ($i = 0; $i < count($nums); $i++) {
            $diff = $target - $nums[$i];
            if (array_key_exists($diff, $arr))
                return [$arr[$diff], $i];
            else
                $arr[$nums[$i]] = $i;
        }
    }
}