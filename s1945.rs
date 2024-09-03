pub struct Solution;

impl Solution {
    /// - Time complexity: O(n + k * log(m))
    /// - Space complexity: O(m)
    pub fn get_lucky(s: String, k: i32) -> i32 {
        let num_str: String = s
            .chars()
            .map(|c| (c as u8 - b'a' + 1).to_string())
            .collect();

        let mut result = num_str
            .chars()
            .map(|c| c.to_digit(10).unwrap())
            .sum::<u32>();

        for _ in 1..k {
            result = result
                .to_string()
                .chars()
                .map(|c| c.to_digit(10).unwrap())
                .sum();
        }

        result as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::get_lucky("iiii".to_string(), 1), 36);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::get_lucky("leetcode".to_string(), 2), 6);
    }

    fn test_3() {
        assert_eq!(Solution::get_lucky("zbax".to_string(), 2), 8);
    }
}
