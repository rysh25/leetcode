pub struct Solution;

impl Solution {
    // - Time complexity: O(q)
    // - Space complexity: O(q)
    pub fn xor_queries(arr: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = arr.len();
        let mut prefix_xor: Vec<i32> = vec![0; n + 1];

        for i in 0..n {
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i];
        }

        let mut ans: Vec<i32> = Vec::new();

        for q in 0..queries.len() {
            ans.push(prefix_xor[queries[q][0] as usize] ^ prefix_xor[queries[q][1] as usize + 1]);
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
            Solution::xor_queries(
                vec![1, 3, 4, 8],
                vec![vec![0, 1], vec![1, 2], vec![0, 3], vec![3, 3]]
            ),
            [2, 7, 14, 8]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::xor_queries(
                vec![4, 8, 2, 10],
                vec![vec![2, 3], vec![1, 3], vec![0, 0], vec![0, 3]]
            ),
            [8, 0, 4, 4]
        );
    }
}
