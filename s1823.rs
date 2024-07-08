pub struct Solution;

impl Solution {
    /// ゲームをしている友達が n 人います。友達は輪になって座っており、時計回りに 1 から n までの番号が付けられています。より正式には、i 番目の友人から時計回りに移動すると、1 = i n の (i+1) 番目の友人に移動し、n 番目の友人から時計回りに移動すると、1 番目の友人に移動します。
    ///
    /// ゲームのルールは次のとおりです。
    ///
    /// 1. 1人目の友達から始めます。
    /// 2. 最初の友達を含めて、時計回りに次の k 人の友達を数えます。カウントは円を一周し、一部の友人は複数回カウントされる場合があります。
    /// 3. あなたが数えた最後の友達はサークルから去り、ゲームに負けます。
    /// 4. サークル内にまだ複数の友達がいる場合は、負けた友達のすぐ右回りに時計回りに手順 2 に戻り、繰り返します。
    /// 5. それ以外の場合は、サークル内の最後の友達がゲームに勝ちます。
    ///
    /// 友達の数 n と整数 k を指定すると、ゲームの勝者を返します。
    ///
    /// - Time complexity: O(nk)
    /// - Space complexity: O(n)
    pub fn find_the_winner(n: i32, k: i32) -> i32 {
        let mut q: std::collections::VecDeque<i32> = std::collections::VecDeque::new();

        for i in 1..=n {
            q.push_back(i);
        }

        while q.len() > 1 {
            let mut x = k;

            while x > 1 {
                let v = q.pop_front();
                q.push_back(v.unwrap());

                x -= 1;
            }
            q.pop_front();
        }

        q.front().copied().unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::find_the_winner(5, 2), 3);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::find_the_winner(6, 5), 1);
    }
}
