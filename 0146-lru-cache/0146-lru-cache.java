class LRUCache {
    class Node{
        Node prev;
        Node next;
        int key;
        int value;
        Node(int k,int v){
            key = k;
            value = v;
        }
    }
    Node head = new Node(0,0);
    Node tail = new Node(0,0);
    Map<Integer,Node> hm = new HashMap();
    int cap = 0;
    public LRUCache(int capacity) {
        cap = capacity;
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if(hm.containsKey(key)){
            Node node = hm.get(key);
            remove(node);
            insert(node);
            return node.value;
        }else{
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if(hm.containsKey(key)){
            remove(hm.get(key));
        }
        if(hm.size()==cap){
            remove(tail.prev);
        }
        insert(new Node(key,value));
    }
    private void remove(Node node){
        hm.remove(node.key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    private void insert(Node node){
        hm.put(node.key,node);
        node.next = head.next;
        node.next.prev = node;
        head.next = node;
        node.prev = head;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */