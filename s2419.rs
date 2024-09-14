use std::cmp::max;

pub struct Solution;

impl Solution {
    /// - Time complexity: O(n)
    /// - Space complexity: O(1)
    ///
    /// #BitManipulation
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mx = *nums.iter().max().unwrap();

        let mut ans = 0;

        let mut streak = 0;

        for i in nums {
            if i == mx {
                streak += 1;
            } else {
                ans = max(ans, streak);
                streak = 0;
            }
        }
        ans = max(ans, streak);

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::longest_subarray(vec![1, 2, 3, 3, 2, 2]), 2);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::longest_subarray(vec![1, 2, 3, 4]), 1);
    }
}
