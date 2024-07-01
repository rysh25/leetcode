pub struct Solution;

impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        let mut odd = 0;

        for n in arr {
            if n % 2 == 1 {
                odd += 1;
            } else {
                odd = 0;
            }

            if odd == 3 {
                return true;
            }
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::three_consecutive_odds(vec![2, 6, 4, 1]), false);
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::three_consecutive_odds(vec![1, 2, 34, 3, 4, 5, 7, 23, 12]),
            true
        );
    }
}
