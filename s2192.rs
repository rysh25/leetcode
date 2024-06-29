pub struct Solution;

impl Solution {
    /// 有向非巡回グラフ (DAG) のノード数を表す正の整数 n が与えられます。ノードには 0 から n - 1 (両端の値を含む) までの番号が付けられます。
    /// また、2D 整数配列edges も与えられます。edges[i] = [fromi, toi] は、グラフ内に from_i から to_i への一方向のエッジがあることを示します。
    /// リストの回答を返します。ここで、answer[i] は、昇順にソートされた i 番目のノードの祖先のリストです。
    /// u がエッジのセットを介して v に到達できる場合、ノード u は別のノード v の祖先になります。
    ///
    /// - Time complexity: O(n^2)
    /// - Space complexity: O(n^2)
    pub fn get_ancestors(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = vec![vec![]; n as usize];

        let mut g: Vec<Vec<i32>> = vec![vec![]; n as usize];

        for edge in edges {
            g[edge[0] as usize].push(edge[1]);
        }

        fn dfs(
            u: i32,
            parent: i32,
            g: &Vec<Vec<i32>>,
            ans: &mut Vec<Vec<i32>>,
            visited: &mut Vec<bool>,
        ) {
            visited[u as usize] = true;

            for v in &g[u as usize] {
                if visited[*v as usize] {
                    continue;
                }
                ans[*v as usize].push(parent);
                dfs(*v, parent, g, ans, visited);
            }
        }

        for i in 0..n {
            let mut visited: Vec<bool> = vec![false; n as usize];
            dfs(i, i, &g, &mut ans, &mut visited);
            // println!("{:?}", ans);
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
            Solution::get_ancestors(
                8,
                vec![
                    vec![0, 3],
                    vec![0, 4],
                    vec![1, 3],
                    vec![2, 4],
                    vec![2, 7],
                    vec![3, 5],
                    vec![3, 6],
                    vec![3, 7],
                    vec![4, 6]
                ]
            ),
            vec![
                vec![],
                vec![],
                vec![],
                vec![0, 1],
                vec![0, 2],
                vec![0, 1, 3],
                vec![0, 1, 2, 3, 4],
                vec![0, 1, 2, 3]
            ]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::get_ancestors(
                5,
                vec![
                    vec![0, 1],
                    vec![0, 2],
                    vec![0, 3],
                    vec![0, 4],
                    vec![1, 2],
                    vec![1, 3],
                    vec![1, 4],
                    vec![2, 3],
                    vec![2, 4],
                    vec![3, 4]
                ]
            ),
            vec![vec![], vec![0], vec![0, 1], vec![0, 1, 2], vec![0, 1, 2, 3]]
        );
    }
}
