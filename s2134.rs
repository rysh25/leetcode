use std::cmp::min;

pub struct Solution;

impl Solution {
    /// - Time complexity: O(n)
    /// - Space complexity: O(1)
    ///
    /// #SlidingWindow
    ///
    /// nums 配列内に存在する1の数をウィンドウサイズとして、スライディングウィンドウで、
    /// そのウィンドウ内に存在する0の数を数える。
    /// 0の数がスワップ回数となるので、その最小値を数える。
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        let count_ones = nums.iter().filter(|&n| *n == 1).count();

        let n = nums.len();

        let mut ans = 1001001001;

        let (mut l, mut r) = (0, 0);

        let mut zeros_in_window = 0;
        while r < count_ones {
            if nums[r] == 0 {
                zeros_in_window += 1;
            }
            r += 1;
        }

        loop {
            // eprintln!(
            //     "l={:?}, r={:?}, zeros_in_window={:?}, count_ones-zeros_in_window={:?}",
            //     l,
            //     r,
            //     zeros_in_window,
            //     count_ones - zeros_in_window
            // );
            ans = min(ans, zeros_in_window);

            r += 1;
            if nums[(r - 1) % n] == 0 {
                zeros_in_window += 1;
            }
            if nums[l] == 0 {
                zeros_in_window -= 1;
            }
            l += 1;
            if l == n {
                break;
            }
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::min_swaps(vec![0, 1, 0, 1, 1, 0, 0]), 1);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::min_swaps(vec![0, 1, 1, 1, 0, 0, 1, 1, 0]), 2);
    }
    #[test]

    fn test_3() {
        assert_eq!(Solution::min_swaps(vec![1, 1, 0, 0, 1]), 0);
    }

    #[test]

    fn test_4() {
        assert_eq!(Solution::min_swaps(vec![1, 1, 1, 0, 0, 1, 0, 1, 1, 0]), 1);
    }
}
