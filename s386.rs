pub struct Solution;

impl Solution {
    // - Time complexity: O(n)
    // - Space complexity: O(1)
    pub fn lexical_order(n: i32) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::new();

        let mut curr = 1;
        for _ in 0..(n as usize) {
            ans.push(curr);

            if curr * 10 <= n {
                curr *= 10;
            } else {
                if curr >= n {
                    curr /= 10;
                }
                curr += 1;
                while curr % 10 == 0 {
                    curr /= 10;
                }
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
        assert_eq!(
            Solution::lexical_order(13),
            [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::lexical_order(2), [1, 2]);
    }
}
