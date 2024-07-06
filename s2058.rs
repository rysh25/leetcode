// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}
pub struct Solution;

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    /// 連結リストにおけるクリティカルポイントは、局所最大値または局所最小値として定義されます。
    ///
    /// ノードが以下の場合、局所最大値です。
    /// - 現在のノードの値が前のノードと次のノードの値よりも厳密に大きい。
    /// ノードが以下の場合、局所最小値です。
    /// - 現在のノードの値が前のノードと次のノードの値よりも厳密に小さい。
    /// 注意：ノードが局所最大値または局所最小値になるためには、前のノードと次のノードの両方が存在する必要があります。
    ///
    /// 連結リストの先頭ノードが与えられた場合、 [minDistance, maxDistance] という長さ2の配列を返します。ここで、minDistanceは任意の2つの異なるクリティカルポイント間の最小距離、maxDistanceは任意の2つの異なるクリティカルポイント間の最大距離です。クリティカルポイントが2つ未満の場合、 [-1, -1] を返します。
    ///
    /// - Time complexity: O(n)
    /// - Space complexity: O(1)
    ///
    /// #LindedList
    pub fn nodes_between_critical_points(head: Option<Box<ListNode>>) -> Vec<i32> {
        let mut ans = vec![-1; 2];

        if head.is_none() {
            return ans;
        }

        let head = head.unwrap();

        let mut prev: i32 = head.val;

        let mut cur = head.next.as_ref();

        if cur.is_none() {
            return ans;
        }

        let mut next = cur.unwrap().next.as_ref();

        let mut min_i = -1;
        let mut prev_i = -1;
        let mut min_d = 1001001001;

        let mut i = 1;

        while next.is_some() {
            if (prev < cur.unwrap().val && cur.unwrap().val > next.unwrap().val)
                || (prev > cur.unwrap().val && cur.unwrap().val < next.unwrap().val)
            {
                if prev_i == -1 {
                    min_i = i;
                } else {
                    min_d = std::cmp::min(min_d, i - prev_i);
                }
                prev_i = i;
            }
            prev = cur.unwrap().val;
            cur = next;
            next = cur.unwrap().next.as_ref();
            i += 1;
        }

        if min_d < 1001001001 {
            ans[0] = min_d;
        }

        if min_i > -1 && prev_i != min_i {
            ans[1] = prev_i - min_i;
        }

        ans
    }
}
