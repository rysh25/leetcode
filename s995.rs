pub struct Solution;

impl Solution {
    pub fn min_k_bit_flips(mut nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..(n + 1 - k as usize) {
            if nums[i] == 0 {
                for j in 0..k as usize {
                    nums[i + j] ^= 1;
                }
                ans += 1;
                // eprintln!("nums={:?}", nums,);
            }
        }

        // eprintln!("nums={:?}", nums,);
        if nums.iter().sum::<i32>() == n as i32 {
            ans
        } else {
            -1
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::min_k_bit_flips(vec![0, 1, 0], 1), 2);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::min_k_bit_flips(vec![1, 1, 0], 2), -1);
    }

    #[test]

    fn test_3() {
        assert_eq!(
            Solution::min_k_bit_flips(vec![0, 0, 0, 1, 0, 1, 1, 0], 3),
            3
        );
    }
}
