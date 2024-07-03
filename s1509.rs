pub struct Solution;

impl Solution {
    /// 整数配列 nums が与えられます。
    /// 1 回の操作で、nums の要素を 1 つ選択し、それを任意の値に変更できます。
    /// 最大 3 つの手を実行した後の nums の最大値と最小値の間の最小差を返します。
    ///
    ///
    /// 最小値と最大値の差をできるだけ小さくなるようにする。そのパターンは、3x3 パターンあるので全て試す。
    ///
    /// - Time complexity: O(n)
    /// - Space complexity: O(1)
    pub fn min_difference(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();

        if n <= 4 {
            return 0;
        }

        nums.sort();

        println!("{:?}", nums);

        let mut ans = 2001001001;

        for l in 0..4 {
            let r = 3 - l;
            println!(
                "l={:?}, r={:?}, nums[l]={:?}, nums[r]={:?}, nums[r]-nums[l]={:?}",
                l,
                r,
                nums[l],
                nums[r],
                nums[r] - nums[l],
            );
            ans = std::cmp::min(ans, nums[n - r - 1] - nums[l]);
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::min_difference(vec![5, 3, 2, 4]), 0);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::min_difference(vec![1, 5, 0, 10, 14]), 1);
    }

    #[test]

    fn test_3() {
        assert_eq!(Solution::min_difference(vec![3, 100, 20]), 0);
    }

    #[test]

    fn test_4() {
        assert_eq!(Solution::min_difference(vec![9, 48, 92, 48, 81, 31]), 17);
    }

    #[test]

    fn test_5() {
        assert_eq!(Solution::min_difference(vec![6, 6, 0, 1, 1, 4, 6]), 2);
    }
}
