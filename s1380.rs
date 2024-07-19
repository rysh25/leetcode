use std::cmp::min;

pub struct Solution;

impl Solution {
    /// - Time complexity: O(nm)
    /// - Space complexity: O(n)
    pub fn lucky_numbers(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let n = matrix.len();
        let m = matrix[0].len();

        let inf = 1001001001;
        let mut mn: Vec<i32> = vec![inf; n];
        for i in 0..n {
            for j in 0..m {
                mn[i] = min(mn[i], matrix[i][j]);
            }
        }

        let mut ans: Vec<i32> = Vec::new();

        for j in 0..m {
            let mut mx = 0;
            let mut mx_i = 0;
            for i in 0..n {
                if mx <= matrix[i][j] {
                    mx = matrix[i][j];
                    mx_i = i;
                }
            }

            if mn[mx_i] == mx {
                ans.push(mx);
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
            Solution::lucky_numbers(vec![vec![3, 7, 8], vec![9, 11, 13], vec![15, 16, 17]]),
            [15]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::lucky_numbers(vec![
                vec![1, 10, 4, 2],
                vec![9, 3, 8, 7],
                vec![15, 16, 17, 12]
            ]),
            [12]
        );
    }
    #[test]

    fn test_3() {
        assert_eq!(Solution::lucky_numbers(vec![vec![7, 8], vec![1, 2]]), [7]);
    }
}
