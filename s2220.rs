pub struct Solution;

impl Solution {
    /// - Time complexity: O(1)
    /// - Space complexity: O(1)
    ///
    /// #BitManipulation
    pub fn min_bit_flips(start: i32, goal: i32) -> i32 {
        let mut xor = start ^ goal;
        let mut ans = 0;

        while xor != 0 {
            ans += xor & 1;
            xor >>= 1;
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::min_bit_flips(10, 7), 3);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::min_bit_flips(3, 4), 3);
    }
}
