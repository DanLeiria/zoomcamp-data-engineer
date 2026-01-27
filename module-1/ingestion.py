import click
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from tqdm.auto import tqdm

### ------------------------------------------------------------------------------------
### Configuration of the data types
### ------------------------------------------------------------------------------------

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64",
}

parse_dates = ["lpep_pickup_datetime", "lpep_dropoff_datetime"]

### ------------------------------------------------------------------------------------
### Main ingestion function
### ------------------------------------------------------------------------------------


@click.command()
@click.option("--pg-user", default="root", help="PostgreSQL user")
@click.option("--pg-pass", default="root", help="PostgreSQL password")
@click.option("--pg-host", default="localhost", help="PostgreSQL host")
@click.option("--pg-port", default=5432, type=int, help="PostgreSQL port")
@click.option("--pg-db", default="ny_taxi", help="PostgreSQL database name")
@click.option("--target-table", default="green_taxi_data", help="Target table name")
@click.option(
    "--chunksize", default=100000, type=int, help="Chunk size for reading Parquet file"
)
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table, chunksize):
    """
    Ingest NYC taxi data into PostgreSQL database.
    """

    ### Initial setup with filepath and database engine
    filepath = "data/green_tripdata_2025-11.parquet"
    engine = create_engine(
        f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}"
    )

    ### Reading the parquet file in chunks
    parquet_file = pq.ParquetFile(filepath)

    ### Ingestion loop - inserting chunks of data
    first = True

    for batch in tqdm(parquet_file.iter_batches(batch_size=chunksize)):
        df_chunk = batch.to_pandas()

        ### Create table with the correct schema and first line
        if first:
            df_chunk.head(0).to_sql(name=target_table, con=engine, if_exists="replace")
            print("Table created")
            first = False

        ### After table is created, insert data in chunks
        df_chunk.to_sql(name=target_table, con=engine, if_exists="append")
        print("Inserted chunk:", len(df_chunk))


if __name__ == "__main__":
    run()
