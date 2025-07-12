using UnityEngine;
using System;

public class Jump : MonoBehaviour
{
    public Rigidbody2D rb;
    public float bounce, speed, teleportAt, happyTimer;
    public KeyCode Left, Right;
    CapsuleSpawner capsuleSpawner;
    [SerializeField] GameObject spawner;
    private bool gravityOn, switch_, right, ending, different;
    public Sprite default_right, default_left, different_right, different_left;
    public BoxCollider2D box;
    private SpriteRenderer spriteRenderer;
    private float checkTimer;
    [SerializeField] private AudioSource jumpSound, endSound;
    EndGame endGame;
    [SerializeField] GameObject endObject;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        spriteRenderer = GetComponent<SpriteRenderer>();
        capsuleSpawner = spawner.GetComponent<CapsuleSpawner>();
        endGame = endObject.GetComponent<EndGame>();
        box = GetComponent<BoxCollider2D>();
        gravityOn = false;
        switch_ = false;
        ending = false;
        different = false;
        checkTimer = happyTimer;
        right = true;
    }


    void Update()
    {
        float x_position = transform.position.x;
        float y_position = transform.position.y;
        if (x_position >= teleportAt + 2.5e-7f)
        {
            transform.position = new Vector2(-teleportAt, transform.position.y);
        }

        else if (x_position <= -teleportAt - 2.5e-7f)
        {
            transform.position = new Vector2(teleportAt, transform.position.y);
        }

        if (y_position >= 5.73 + 2.5e-7f & !ending)
        {
            endSound.Play();
            capsuleSpawner.End();
            rb.constraints = RigidbodyConstraints2D.FreezePosition;
            ending = true;
            spriteRenderer.enabled = false;
            endGame.Game_Over();
        }

        if(checkTimer > 0) {checkTimer -= Time.deltaTime;}
        else if (switch_)
        {
            if (right) {spriteRenderer.sprite = default_right;}
            else {spriteRenderer.sprite = default_left;}

            switch_ = false;
            different = false;
        }
    }


    void OnCollisionEnter2D(Collision2D col)
    {
        if (col.collider.tag == "Capsule")
        {
            if (gravityOn || rb.velocity.y <= capsuleSpawner.capsuleSpeed)
            {
                if (right) {spriteRenderer.sprite = different_right;}
                else {spriteRenderer.sprite = different_left;}

                checkTimer = happyTimer;
                switch_ = true;
                different = true;
                jumpSound.Play();
                rb.velocity = new Vector2(rb.velocity.x, bounce + capsuleSpawner.capsuleSpeed);
                if(gravityOn)
                {
                    capsuleSpawner.NormalPhysics();
                    gravityOn = false;
                }
            }
        }

        else
        {
            capsuleSpawner.FallingPhysics();
            gravityOn = true;
        }
    }


    void OnCollisionStay2D(Collision2D col)
    {
        if (col.collider.tag == "Capsule")
        {
            if (gravityOn || rb.velocity.y <= capsuleSpawner.capsuleSpeed)
            {
                if (right) {spriteRenderer.sprite = different_right;}
                else {spriteRenderer.sprite = different_left;}

                checkTimer = happyTimer;
                switch_ = true;
                different = true;
                jumpSound.Play();
                rb.velocity = new Vector2(rb.velocity.x, bounce + capsuleSpawner.capsuleSpeed);
                if(gravityOn)
                {
                    capsuleSpawner.NormalPhysics();
                    gravityOn = false;
                }
            }
        }

        else if (gravityOn) {capsuleSpawner.DragPhysics();}
        else
        {
            capsuleSpawner.FallingPhysics();
            gravityOn = true;
        }
    }
    

    // Update is called once per frame
    void FixedUpdate()
    {
        if (Input.GetKey(Left)) 
        {
            if (different) {spriteRenderer.sprite = different_left;}
            else {spriteRenderer.sprite = default_left;}

            box.offset = new Vector2(-0.05f, box.offset.y);
            right = false;
            rb.velocity = new Vector2(-speed, rb.velocity.y);
        }
        
        else if (Input.GetKey(Right)) 
        {
            if (different) {spriteRenderer.sprite = different_right;}
            else {spriteRenderer.sprite = default_right;}
            box.offset = new Vector2(0.05f, box.offset.y);
            right = true;
            rb.velocity = new Vector2(speed, rb.velocity.y);
        }

        else {rb.velocity = new Vector2(0, rb.velocity.y);}
    }
}
