use std::{cmp::max, collections::VecDeque};

pub struct Solution;

impl Solution {
    /// 整数 num の配列と整数 limit が指定されます。
    /// この部分配列の 2 つの要素間の絶対差が limit 以下になる最長の空でない部分配列のサイズを返します。
    ///
    /// - Time complexity: O(n)
    /// - Space complexity: O(n)
    ///
    /// #SlidingWindow
    pub fn longest_subarray(nums: Vec<i32>, limit: i32) -> i32 {
        let mut l = 0 as usize;

        let mut dec_deq: VecDeque<i32> = VecDeque::new();
        let mut inc_deq: VecDeque<i32> = VecDeque::new();

        let mut ans: i32 = 0;

        for r in 0..nums.len() {
            // println!(
            //     "dec_deq={:?}, inc_deq={:?}, limit={:?}",
            //     dec_deq, inc_deq, limit
            // );
            while !dec_deq.is_empty() && dec_deq.back().unwrap() < &nums[r] {
                dec_deq.pop_back();
            }
            dec_deq.push_back(nums[r]);

            while !inc_deq.is_empty() && inc_deq.back().unwrap() > &nums[r] {
                inc_deq.pop_back();
            }
            inc_deq.push_back(nums[r]);

            // println!(
            //     "dec_deq={:?}, inc_deq={:?}, limit={:?}",
            //     dec_deq, inc_deq, limit
            // );
            while dec_deq[0] - inc_deq[0] > limit {
                if dec_deq[0] == nums[l] {
                    dec_deq.pop_front();
                }

                if inc_deq[0] == nums[l] {
                    inc_deq.pop_front();
                }

                l += 1;
            }
            // println!(
            //     "dec_deq={:?}, inc_deq={:?}, limit={:?}",
            //     dec_deq, inc_deq, limit
            // );

            // println!("ans={:?}, l={:?}, r={:?}", ans, l, r);

            ans = max(ans, (r - l + 1) as i32);
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::longest_subarray(vec![8, 2, 4, 7], 4), 2);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::longest_subarray(vec![10, 1, 2, 4, 7, 2], 5), 4);
    }

    #[test]

    fn test_3() {
        assert_eq!(
            Solution::longest_subarray(vec![4, 2, 2, 2, 4, 4, 2, 2], 0),
            3
        );
    }
}
