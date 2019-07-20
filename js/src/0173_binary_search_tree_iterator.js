/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 */
let BSTIterator = function (root) {
  this.nodes = []
  this.pushLeftNodes(root)
};

/**
 * Push node and it's all left
 *
 *
 * @param {TreeNode|null} node
 */
BSTIterator.prototype.pushLeftNodes = function (node) {
  while (node !== null) {
    this.nodes.push(node)
    node = node.left
  }
}

/**
 * @return the next smallest number
 * @return {number}
 */
BSTIterator.prototype.next = function () {
  let next = this.nodes.pop()
  this.pushLeftNodes(next.right)

  return next.val
};

/**
 * @return whether we have a next smallest number
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function () {
  return this.nodes.length !== 0
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */