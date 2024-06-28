pub struct Solution;

impl Solution {
    /// 国の都市の数を示す整数 n が与えられます。都市には 0 から n - 1 までの番号が付けられます。
    /// また、2D 整数配列 Roads も与えられます。ここで、Roads[i] = [a_i, b_i] は、都市 a_i と b_i を結ぶ双方向の道路が存在することを示します。
    ///
    /// 各都市に 1 から n までの整数値を割り当てる必要があります。
    /// 各値は 1 回だけ使用できます。道路の重要性は、道路が接続する 2 つの都市の値の合計として定義されます。
    ///
    /// 値を最適に割り当てた後、可能なすべての道路の最大合計重要度を返します。
    ///
    /// - Time complexity: O(n log n + m)
    /// - Space complexity: O(n + m)
    ///
    /// #Greedy
    /// #Graph
    pub fn maximum_importance(n: i32, roads: Vec<Vec<i32>>) -> i64 {
        let mut cities: Vec<(i32, usize)> = (0..n).map(|i| (0, i as usize)).collect();

        for road in &roads {
            cities[road[0] as usize].0 += 1;
            cities[road[1] as usize].0 += 1;
        }

        cities.sort();

        let mut importance: Vec<i64> = vec![0; n as usize];

        for (i, city) in cities.iter().enumerate() {
            importance[city.1] = (i + 1) as i64;
        }

        // eprintln!("importance={:?}", importance);

        let mut ans: i64 = 0;
        for road in &roads {
            ans += importance[road[0] as usize] + importance[road[1] as usize];
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
            Solution::maximum_importance(
                5,
                vec![
                    vec![0, 1],
                    vec![1, 2],
                    vec![2, 3],
                    vec![0, 2],
                    vec![1, 3],
                    vec![2, 4]
                ]
            ),
            43
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::maximum_importance(5, vec![vec![0, 3], vec![2, 4], vec![1, 3]]),
            20
        );
    }
}
