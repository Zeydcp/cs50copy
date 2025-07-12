using UnityEngine;

public class CapsulePhysics : MonoBehaviour
{
    public Rigidbody2D cb;
    public float baseSpeed;

    // Start is called before the first frame update
    void Awake()
    {
        cb = GetComponent<Rigidbody2D>();
        cb.velocity = new Vector2(0, baseSpeed);
    }

}
