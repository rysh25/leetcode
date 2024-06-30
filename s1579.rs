pub struct Solution;

struct UnionFind {
    par: Vec<usize>,
    siz: Vec<usize>,
    components: usize,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            par: (0..n).collect(),
            siz: vec![1; n],
            components: n,
        }
    }

    fn root(&mut self, x: usize) -> usize {
        if self.par[x] == x {
            return x;
        }
        self.par[x] = self.root(self.par[x]);
        self.par[x]
    }

    fn issame(&mut self, x: usize, y: usize) -> bool {
        self.root(x) == self.root(y)
    }

    fn unite(&mut self, mut parent: usize, mut child: usize) -> bool {
        parent = self.root(parent);
        child = self.root(child);

        if parent == child {
            return false;
        }

        if self.siz[parent] < self.siz[child] {
            std::mem::swap(&mut parent, &mut child);
        }

        self.par[child] = parent;
        self.siz[parent] += self.siz[child];

        self.components -= 1;
        true
    }

    fn size(&mut self, x: usize) -> usize {
        let root = self.root(x);
        self.siz[root]
    }

    fn is_connected(&self) -> bool {
        self.components == 1
    }
}

impl Solution {
    /// アリスとボブには、n 個のノードと 3 種類のエッジからなる無向グラフがあります。
    ///
    /// - タイプ 1: アリスのみが通過できます。
    /// - タイプ 2: ボブのみが通過できます。
    /// - タイプ 3: アリスとボブの両方が通過できます。
    ///
    /// edges[i] = [typei, u_i, v_i] がノード u_i と v_i の間の type_i の双方向エッジを表す配列 edges が指定されます。
    /// エッジを削除した後もアリスとボブの両方によって完全に横断されるグラフを維持できるように、削除できるエッジの最大数を見つけます。
    /// 完全に横断されるグラフとは、いずれかのノードから開始すると、アリスとボブはグラフを他のすべてのノードに到達できることをいいます。
    /// 削除できるエッジの最大数を返すか、アリスとボブがグラフを完全に横断できない場合は -1 を返します。
    ///
    ///
    /// アリス用とボブ用の UnionFind 使い必要ななエッジの数を求めます。
    /// まずエッジ タイプ3 のエッジについてアリス用ボブ用の UnionFind をそれぞれ unite し、必要なエッジの数を足します。すでに同じ親の場合はエッジを足しません。
    /// 次にタイプ1について、アリス用の UnionFind に、タイプ2についてボブ用の UnionFind に同様の処理をします。
    /// 処理が終わったらアリス用ボブ用の UnionFind がどちらか一方でも連結成分が1でなければ -1 を返します。
    /// そして、edges の大きあから必要なエッジの数を引くと削除可能なエッジの数が求められます。
    ///
    ///
    /// - Time complexity: O(E * log n)
    /// - Space compleixty: O(n + E)
    pub fn max_num_edges_to_remove(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let (mut alice, mut bob) = (UnionFind::new(n as usize), UnionFind::new(n as usize));

        let mut edges_required = 0;

        let mut edges = edges.clone();

        for edge in &mut edges {
            edge[1] -= 1;
            edge[2] -= 1;
        }

        for edge in &edges {
            if edge[0] == 3
                && alice.unite(edge[1] as usize, edge[2] as usize)
                    | bob.unite(edge[1] as usize, edge[2] as usize)
            {
                edges_required += 1;
            }
        }

        for edge in &edges {
            if edge[0] == 1 {
                if alice.unite(edge[1] as usize, edge[2] as usize) {
                    edges_required += 1;
                }
            } else if edge[0] == 2 && bob.unite(edge[1] as usize, edge[2] as usize) {
                edges_required += 1;
            }
        }

        if alice.is_connected() && bob.is_connected() {
            return (edges.len() - edges_required) as i32;
        }
        -1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::max_num_edges_to_remove(
                4,
                vec![
                    vec![3, 1, 2],
                    vec![3, 2, 3],
                    vec![1, 1, 3],
                    vec![1, 2, 4],
                    vec![1, 1, 2],
                    vec![2, 3, 4]
                ]
            ),
            2
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::max_num_edges_to_remove(
                4,
                vec![vec![3, 1, 2], vec![3, 2, 3], vec![1, 1, 4], vec![2, 1, 4]]
            ),
            0
        );
    }

    fn test_3() {
        assert_eq!(
            Solution::max_num_edges_to_remove(4, vec![vec![3, 2, 3], vec![1, 1, 2], vec![2, 3, 4]]),
            -1
        );
    }
}
