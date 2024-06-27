pub struct Solution;

impl Solution {
    /// 1 から n までのラベルが付けられた n 個のノードで構成される無向スター グラフがあります。スター グラフは、1 つの中心ノードと、その中心ノードを他のすべてのノードに接続する正確に n - 1 個のエッジがあるグラフです。
    /// 2D 整数配列のedgesが与えられます。各edges[i] = [ui, vi]は、ノードuiとviの間にエッジがあることを示します。指定された星形グラフの中心を返します。
    ///
    /// - Time complexity: O(n)
    /// - Space complexity: O(n)
    ///
    /// #Graph
    pub fn find_center(edges: Vec<Vec<i32>>) -> i32 {
        let n = edges.len() + 1;
        let mut degrees: Vec<i32> = vec![0; n + 1];

        for edge in edges {
            degrees[edge[0] as usize] += 1;
            degrees[edge[1] as usize] += 1;
        }

        degrees
            .iter()
            .enumerate()
            .find(|&(_, &degree)| degree == (n - 1) as i32)
            .map(|(i, _)| i as i32)
            .unwrap_or(-1)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::find_center(vec![vec![1, 2], vec![2, 3], vec![4, 2]]),
            2
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::find_center(vec![vec![1, 2], vec![5, 1], vec![1, 3], vec![1, 4]]),
            1
        );
    }
}
