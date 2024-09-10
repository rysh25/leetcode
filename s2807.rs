pub struct Solution;
// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//   dd    next: None,
//       val
//     }
//   }
// }

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let temp = b;
        b = a % b;
        a = temp;
    }
    a.abs()
}

impl Solution {
    /// - Time complexity: O(n * log(v))
    /// - Space comlexity: O(n)
    ///
    /// LinkedList
    pub fn insert_greatest_common_divisors(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head = head?;
        let mut curr = &mut *head;

        while let Some(next) = curr.next.take() {
            let g = gcd(curr.val as i64, next.val as i64);

            let mut new_node = Box::new(ListNode::new(g as i32));
            curr = curr.next.insert(new_node).next.insert(next);
        }

        head.into()
    }
}
