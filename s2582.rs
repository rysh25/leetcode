pub struct Solution;

impl Solution {
    /// n 人の人が 1 から n までのラベルが付けられた列に並んでいます。列の先頭の人は最初は枕を持っています。
    /// 枕を持っている人は毎秒、列に並んでいる次の人に枕を渡します。枕が列の最後尾に達すると方向が変わり、人々は反対方向に枕を渡し続けます。
    ///
    /// - Time complexity: O(n)
    /// - Space complexity: O(1)
    ///
    /// #Math
    pub fn pass_the_pillow(n: i32, time: i32) -> i32 {
        let r = time % (n - 1);

        if time / (n - 1) % 2 == 0 {
            r + 1
        } else {
            n - r
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::pass_the_pillow(4, 5), 2);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::pass_the_pillow(3, 2), 3);
    }

    #[test]

    fn test_3() {
        assert_eq!(Solution::pass_the_pillow(18, 38), 5);
    }

    #[test]

    fn test_4() {
        assert_eq!(Solution::pass_the_pillow(26, 1000), 1);
    }
}
