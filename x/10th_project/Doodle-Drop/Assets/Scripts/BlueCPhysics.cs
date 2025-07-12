using UnityEngine;

public class BlueCPhysics : MonoBehaviour
{
    public Rigidbody2D cb;
    public float baseSpeed;
    public float x_speed;

    // Start is called before the first frame update
    void Awake()
    {
        cb = GetComponent<Rigidbody2D>();
        cb.velocity = new Vector2(x_speed, baseSpeed);
    }


    void FixedUpdate()
    {
        float x_position = transform.position.x;
        if (x_position >= 2.56) {cb.velocity = new Vector2(-x_speed, cb.velocity.y);}
        else if (x_position <= -2.56) {cb.velocity = new Vector2(x_speed, cb.velocity.y);}
    }
}
