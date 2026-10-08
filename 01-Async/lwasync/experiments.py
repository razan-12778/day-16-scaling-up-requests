from lwasync.client_asynchronous import generate_statistics_async


def experiment(n_calls: int, url: str):
    print(f"\nThis expirment on {n_calls} calls returned:")
    stats, duration = generate_statistics_async(n_calls, url)
    print("Statistics:")
    print(f"{stats}")
    print(f"Total duration: \t{duration:0.6f}")
    return stats, duration


if __name__ == "__main__":
    gcp_api_base = "https://lwasync-795589155447.europe-west1.run.app"
    endpoint = "/fast-run"
    api_url = gcp_api_base + endpoint
    experiment(25, api_url)
