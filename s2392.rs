use std::collections::VecDeque;

pub struct Solution;

impl Solution {
    /// - Time complexity: O(n+k)
    /// - Space complexity: O(k^2)
    ///
    /// #TopologicalSort
    /// #BFS
    pub fn build_matrix(
        k: i32,
        row_conditions: Vec<Vec<i32>>,
        col_conditions: Vec<Vec<i32>>,
    ) -> Vec<Vec<i32>> {
        let mut row_g: Vec<Vec<i32>> = vec![Vec::new(); k as usize];
        for r in &row_conditions {
            row_g[(r[0] - 1) as usize].push(r[1] - 1);
        }
        // eprintln!("row_g={:?}", row_g);

        let mut col_g: Vec<Vec<i32>> = vec![Vec::new(); k as usize];
        for c in &col_conditions {
            col_g[(c[0] - 1) as usize].push(c[1] - 1);
        }
        // eprintln!("col_g={:?}", col_g);
        let row_sorted = Self::topological_sort(row_g);
        // eprintln!("row_sorted={:?}", row_sorted);
        if row_sorted.is_empty() {
            return Vec::new();
        }

        let col_sorted = Self::topological_sort(col_g);
        // eprintln!("col_sorted={:?}", col_sorted);
        if col_sorted.is_empty() {
            return Vec::new();
        }

        let mut col_idx: Vec<usize> = vec![0; k as usize];

        for (i, &col) in col_sorted.iter().enumerate() {
            col_idx[col] = i;
        }

        // eprintln!("col_map={:?}", col_map);

        let mut ans: Vec<Vec<i32>> = vec![vec![0; k as usize]; k as usize];

        for &i in &row_sorted {
            ans[i][col_idx[row_sorted[i]]] = (row_sorted[i] + 1) as i32;
        }

        ans
    }

    fn topological_sort(g: Vec<Vec<i32>>) -> Vec<usize> {
        let mut sorted_verticies: Vec<usize> = Vec::new();
        let mut indegrees: Vec<i32> = vec![0; g.len()];

        for v in &g {
            for &to in v {
                indegrees[to as usize] += 1;
            }
        }

        // eprintln!("indegrees={:?}", indegrees);

        let mut q: VecDeque<i32> = VecDeque::new();

        for (i, ind) in indegrees.iter().enumerate() {
            if *ind == 0 {
                q.push_back(i as i32);
            }
        }

        while !q.is_empty() {
            let cur = q.pop_front();

            let cur = cur.unwrap();

            sorted_verticies.push(cur as usize);

            for &n in &g[cur as usize] {
                indegrees[n as usize] -= 1;

                if indegrees[n as usize] == 0 {
                    q.push_back(n);
                }
            }
        }

        if sorted_verticies.len() != g.len() {
            return Vec::new();
        }

        sorted_verticies
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::build_matrix(
                3,
                vec![vec![1, 2], vec![3, 2]],
                vec![vec![2, 1], vec![3, 2]]
            ),
            [[3, 0, 0], [0, 0, 1], [0, 2, 0]]
        );
    }

    #[test]

    fn test_2() {
        let v: Vec<Vec<i32>> = Vec::new();
        assert_eq!(
            Solution::build_matrix(
                3,
                vec![vec![1, 2], vec![2, 3], vec![3, 1], vec![2, 3]],
                vec![vec![2, 1]]
            ),
            v
        );
    }
}
