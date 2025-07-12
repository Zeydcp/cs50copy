using System.Collections.Generic;
using UnityEngine;
using System;

public class CapsuleSpawner : MonoBehaviour
{
    public GameObject Spawner;
    public GameObject Bspawner;
    public Vector2 minPosition, maxPosition;
    public int minCubes, maxCubes;
    private List<GameObject> Capsules = new List<GameObject>();
    private Rigidbody2D rb;
    public float EraseAt, fallingSpeed;
    CapsulePhysics capsulePhysics;
    BlueCPhysics blueCPhysics;
    private GameObject consistent;
    private bool check = true;
    private float height;
    [HideInInspector] public int scores;
    [HideInInspector] public float capsuleSpeed;
    public Transform Merge;
    public GameObject MergeObject;


    // Start is called before the first frame update
    void Start()
    {
        scores = 0;
        capsulePhysics = Spawner.GetComponent<CapsulePhysics>();
        blueCPhysics = Bspawner.GetComponent<BlueCPhysics>();
        MergeObject.SetActive(false);
        capsuleSpeed = capsulePhysics.baseSpeed;
        int n = UnityEngine.Random.Range(minCubes, maxCubes + 1);
        float[] x_array = {-2.56f, -1.28f, 0, 1.28f, 2.56f};
        int length = x_array.Length;
        for (int i = 0; i < n; i++)
        {
            int index = UnityEngine.Random.Range(0, length);
            float x = x_array[index];
            float y = UnityEngine.Random.Range(minPosition.y, maxPosition.y);
            y = (float) Math.Round(y * 3, MidpointRounding.AwayFromZero) / 3;
            Vector2 randomSpawnPosition = new Vector2(x, y);
            int count = Capsules.Count;
            for (int j = 0; j < count; j++)
            {
                while (randomSpawnPosition == (Vector2) Capsules[j].transform.position)
                {
                    j = 0;
                    index = UnityEngine.Random.Range(0, length);
                    x = x_array[index];
                    y = UnityEngine.Random.Range(minPosition.y, maxPosition.y);
                    y = (float) Math.Round(y * 3, MidpointRounding.AwayFromZero) / 3;
                    randomSpawnPosition = new Vector2(x, y);
                }
            }
            GameObject Capsule = Instantiate(Spawner, randomSpawnPosition, Quaternion.identity);
            Capsules.Add(Capsule);
        }
    }


    // Update is called once per frame
    void Update()
    {
        for (int i = Capsules.Count - 1; i >= 0; i--)
        {
            float position = Capsules[i].transform.position.y;
            if (position >= EraseAt) 
            {
                Destroy(Capsules[i]);
                Capsules.RemoveAt(i);
                scores += 1;
            }

            else if(position <= -5 & check)
            {
                consistent = Capsules[i];
                height = consistent.transform.position.y + 10.24f;
                check = false;
            }
        }

        if (consistent.transform.position.y >= height)
        {
            int n = UnityEngine.Random.Range(5, 9);
            int l = (int) Math.Round(UnityEngine.Random.Range(n * 0.6f, n + 1));
            int m = n - l;
            float[] x_array = {-2.56f, -1.28f, 0, 1.28f, 2.56f};
            int length = x_array.Length;
            if (scores >= 750)
            {
                for (int i = 0; i < l; i++)
                {
                    int index = UnityEngine.Random.Range(0, length);
                    float x = x_array[index];
                    float y = UnityEngine.Random.Range(minPosition.y, maxPosition.y - 18.432f);
                    y = (float) Math.Round(y * 3, MidpointRounding.AwayFromZero) / 3;
                    Vector2 randomSpawnPosition = new Vector2(x, y);
                    int count = Capsules.Count;
                    for (int j = 0; j < count; j++)
                    {
                        while (randomSpawnPosition == (Vector2) Capsules[j].transform.position)
                        {
                            j = 0;
                            index = UnityEngine.Random.Range(0, length);
                            x = x_array[index];
                            y = UnityEngine.Random.Range(minPosition.y, maxPosition.y - 18.432f);
                            y = (float) Math.Round(y * 3, MidpointRounding.AwayFromZero) / 3;
                            randomSpawnPosition = new Vector2(x, y);
                        }
                    }
                    GameObject Capsule = Instantiate(Spawner, randomSpawnPosition, Quaternion.identity);
                    Capsules.Add(Capsule);
                    Rigidbody2D rb = Capsule.GetComponent<Rigidbody2D>();
                    rb.velocity = new Vector2(0, Capsules[0].GetComponent<Rigidbody2D>().velocity.y);
                    rb.gravityScale = Capsules[0].GetComponent<Rigidbody2D>().gravityScale;
                }

                for (int i = 0; i < m; i++)
                {
                    int index = UnityEngine.Random.Range(0, length);
                    float x = x_array[index];
                    float y = UnityEngine.Random.Range(minPosition.y, maxPosition.y - 18.432f);
                    y = (float) Math.Round(y * 3, MidpointRounding.AwayFromZero) / 3;
                    Vector2 randomSpawnPosition = new Vector2(x, y);
                    int count = Capsules.Count;
                    for (int j = 0; j < count; j++)
                    {
                        while (randomSpawnPosition.y == Capsules[j].transform.position.y)
                        {
                            j = 0;
                            y = UnityEngine.Random.Range(minPosition.y, maxPosition.y - 18.432f);
                            y = (float) Math.Round(y * 3, MidpointRounding.AwayFromZero) / 3;
                            randomSpawnPosition = new Vector2(x, y);
                        }
                    }
                    GameObject Capsule = Instantiate(Bspawner, randomSpawnPosition, Quaternion.identity);
                    Capsules.Add(Capsule);
                    Rigidbody2D rb = Capsule.GetComponent<Rigidbody2D>();
                    rb.velocity = new Vector2(rb.velocity.x, Capsules[0].GetComponent<Rigidbody2D>().velocity.y);
                    rb.gravityScale = Capsules[0].GetComponent<Rigidbody2D>().gravityScale;
                }
            }

            else
            {
                for (int i = 0; i < n; i++)
                {
                    int index = UnityEngine.Random.Range(0, length);
                    float x = x_array[index];
                    float y = UnityEngine.Random.Range(minPosition.y, maxPosition.y - 18.432f);
                    y = (float) Math.Round(y * 3, MidpointRounding.AwayFromZero) / 3;
                    Vector2 randomSpawnPosition = new Vector2(x, y);
                    int count = Capsules.Count;
                    for (int j = 0; j < count; j++)
                    {
                        while (randomSpawnPosition == (Vector2) Capsules[j].transform.position)
                        {
                            j = 0;
                            index = UnityEngine.Random.Range(0, length);
                            x = x_array[index];
                            y = UnityEngine.Random.Range(minPosition.y, maxPosition.y - 18.432f);
                            y = (float) Math.Round(y * 3, MidpointRounding.AwayFromZero) / 3;
                            randomSpawnPosition = new Vector2(x, y);
                        }
                    }
                    GameObject Capsule = Instantiate(Spawner, randomSpawnPosition, Quaternion.identity);
                    Capsules.Add(Capsule);
                    Rigidbody2D rb = Capsule.GetComponent<Rigidbody2D>();
                    rb.velocity = new Vector2(0, Capsules[0].GetComponent<Rigidbody2D>().velocity.y);
                    rb.gravityScale = Capsules[0].GetComponent<Rigidbody2D>().gravityScale;
                }
            }

            check = true;
        }

        if (scores <= 1500) {capsuleSpeed = capsulePhysics.baseSpeed + 2e-3f * scores;}
    }


    public void FallingPhysics()
    {
        int n = Capsules.Count;
        for (int i = 0; i < n; i++) 
        {
            rb = Capsules[i].GetComponent<Rigidbody2D>();
            rb.velocity = new Vector2(rb.velocity.x, fallingSpeed * capsuleSpeed);
            rb.gravityScale = -1;
        }
    }


    public void NormalPhysics()
    {
        int n = Capsules.Count;
        for (int i = 0; i < n; i++)
        {
            rb = Capsules[i].GetComponent<Rigidbody2D>();
            rb.velocity = new Vector2(rb.velocity.x, capsuleSpeed);
            rb.gravityScale = 0;
        }
    }


    public void DragPhysics()
    {
        if (Capsules[0].GetComponent<Rigidbody2D>().velocity.y > 20)
        {
            int n = Capsules.Count;
            for (int i = 0; i < n; i++)
            {
                rb = Capsules[i].GetComponent<Rigidbody2D>();
                rb.gravityScale = 0;
            }
        }
    }

    public void End()
    {
        int n = Capsules.Count;
        for (int i = 0; i < n; i++)
        {
            rb = Capsules[i].GetComponent<Rigidbody2D>();
            rb.constraints = RigidbodyConstraints2D.FreezePosition;
        }
    }

    public void Kid()
    {
        int n = Capsules.Count;
        for (int i = 0; i < n; i++) {Capsules[i].transform.SetParent(Merge);}
    }
}
