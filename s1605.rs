use std::cmp::min;

pub struct Solution;

impl Solution {
    /// - Time complexity: O(nm)
    /// - Space complexity: O(nm)
    ///
    /// #Greedy
    pub fn restore_matrix(mut row_sum: Vec<i32>, mut col_sum: Vec<i32>) -> Vec<Vec<i32>> {
        let n = row_sum.len();
        let m = col_sum.len();

        let mut ans: Vec<Vec<i32>> = vec![vec![0; m]; n];

        for i in 0..n {
            for j in 0..m {
                ans[i][j] = min(row_sum[i], col_sum[j]);
                row_sum[i] -= ans[i][j];
                col_sum[j] -= ans[i][j];
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
            Solution::restore_matrix(vec![3, 8], vec![4, 7]),
            [[3, 0], [1, 7]]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::restore_matrix(vec![5, 7, 10], vec![8, 6, 8]),
            [[0, 5, 0], [6, 1, 0], [2, 0, 8]]
        );
    }
}
