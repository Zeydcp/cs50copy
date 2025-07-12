using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class menuJump : MonoBehaviour
{
    public Rigidbody2D rb;
    public Sprite default_right, different_right;
    public float bounce, happyTimer;
    private float checkTimer;
    private SpriteRenderer spriteRenderer;
    [SerializeField] private AudioSource jumpSound;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        spriteRenderer = GetComponent<SpriteRenderer>();
        checkTimer = happyTimer;
    }

    // Update is called once per frame
    void Update()
    {
        if(checkTimer > 0) {checkTimer -= Time.deltaTime;}
        else {spriteRenderer.sprite = default_right;}
    }

    void OnCollisionEnter2D()
    {
        checkTimer = happyTimer;
        jumpSound.Play();
        spriteRenderer.sprite = different_right;
        rb.velocity = new Vector2(0, bounce);
    }

    void OnCollisionStay2D()
    {
        checkTimer = happyTimer;
        jumpSound.Play();
        spriteRenderer.sprite = different_right;
        rb.velocity = new Vector2(0, bounce);
    }
}
