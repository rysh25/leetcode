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

impl Solution {
    /// - Time complexity: O(n)
    /// - Space complexity: O(n)
    ///
    /// #LinkedList
    pub fn split_list_to_parts(head: Option<Box<ListNode>>, k: i32) -> Vec<Option<Box<ListNode>>> {
        let mut ans: Vec<Option<Box<ListNode>>> = Vec::new();

        let mut curr = head.as_ref();
        let mut n = 0;

        while let Some(node) = curr {
            n += 1;
            curr = node.next.as_ref();
        }

        let (base_size, mut extra) = (n / k, n % k);
        let mut curr = head;

        for _ in 0..k {
            let mut part_size = base_size + if extra > 0 { 1 } else { 0 };
            let mut dummy = Box::new(ListNode { val: 0, next: None });
            let mut tail = &mut dummy;

            while part_size > 0 {
                tail.next = curr.take();
                tail = tail.next.as_mut().unwrap();
                curr = tail.next.take();
                part_size -= 1;
            }

            ans.push(dummy.next.take());
            if extra > 0 {
                extra -= 1;
            }
        }

        ans
    }
}
