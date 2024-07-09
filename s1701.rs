pub struct Solution;

impl Solution {
    /// 一人のシェフがいるレストランがあります。配列 customer が与えられます。customers[i] = [deliveryi, timei]:
    ///
    /// 到着 i は i 番目の顧客の到着時刻です。到着時刻は降順ではない順に並べられます
    /// time_i は、i 番目の顧客の注文を準備するのに必要な時間です。
    /// お客さんが来たら注文を受け、オーダーを通してシェフが仕事を始めるです。顧客はシェフが注文の準備を終えるまで待ちます。シェフは一度に複数のお客様の料理を準備することはありません。シェフは、入力された順序で顧客のために料理を調理します。
    /// すべての顧客の平均待ち時間を返します。
    ///
    /// - Time complexity: O(n)
    /// - Space complexity: O(1)
    ///
    /// #Greedy
    /// #Simulation
    pub fn average_waiting_time(customers: Vec<Vec<i32>>) -> f64 {
        let n = customers.len();
        let mut waiting_time: i64 = 0;
        let mut available_time: i64 = 0;

        for c in customers {
            available_time = std::cmp::max(available_time, c[0] as i64) + c[1] as i64;
            waiting_time += (available_time - c[0] as i64);
        }

        waiting_time as f64 / n as f64
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::average_waiting_time(vec![vec![1, 2], vec![2, 5], vec![4, 3]]),
            5.00000
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::average_waiting_time(vec![vec![5, 2], vec![5, 4], vec![10, 3], vec![20, 1]]),
            3.25000
        );
    }
}
