import React from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import Plot from 'react-plotly.js';
import './RelativeStrength.css';

interface RelativeStrength {
    datetime: string;
    USD: number;
    EUR: number;
    JPY: number;
    GBP: number;
    CHF: number;
}

const fetchStrengths = async (): Promise<RelativeStrength[]> => {
    const { data } = await axios.get<RelativeStrength[]>("http://127.0.0.1:5000/api/strengths/max_daily");
    return data;
};

const StrengthsList: React.FC = () => {
    const { data, error, isLoading } = useQuery<RelativeStrength[]>({
        queryKey: ['strengths'],
        queryFn: fetchStrengths
    });

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>An error occurred: {(error as Error).message}</div>;

    const latestFiveData = data ? data.slice(-5).reverse() : [];

    return (
        <div>
            <h2>Relative Currency Strenghts Over Time</h2>
            <Plot
                data={[
                    {
                        x: data?.map(d => new Date(d.datetime)),
                        y: data?.map(d => d.USD),
                        type: 'scatter',
                        mode: 'lines+points',
                        marker: { color: 'blue' },
                        name: 'USD',
                    },
                    {
                        x: data?.map(d => new Date(d.datetime)),
                        y: data?.map(d => d.EUR),
                        type: 'scatter',
                        mode: 'lines+points',
                        marker: { color: 'green' },
                        name: 'EUR',
                    },
                    {
                        x: data?.map(d => new Date(d.datetime)),
                        y: data?.map(d => d.JPY),
                        type: 'scatter',
                        mode: 'lines+points',
                        marker: { color: 'red' },
                        name: 'JPY',
                    },
                    {
                        x: data?.map(d => new Date(d.datetime)),
                        y: data?.map(d => d.GBP),
                        type: 'scatter',
                        mode: 'lines+points',
                        marker: { color: 'purple' },
                        name: 'GBP',
                    },
                    {
                        x: data?.map(d => new Date(d.datetime)),
                        y: data?.map(d => d.CHF),
                        type: 'scatter',
                        mode: 'lines+points',
                        marker: { color: 'orange' },
                        name: 'CHF',
                    }
                ]}
                layout={{ title: 'Relative Strengths' }}
            />
            <div className="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>USD</th>
                            <th>EUR</th>
                            <th>JPY</th>
                            <th>GBP</th>
                            <th>CHF</th>
                        </tr>
                    </thead>
                    <tbody>
                        {latestFiveData.map((strength: RelativeStrength) => (
                            <tr key={strength.datetime}>
                                <td>{new Date(strength.datetime).toLocaleDateString()}</td>
                                <td>{strength.USD}</td>
                                <td>{strength.EUR}</td>
                                <td>{strength.JPY}</td>
                                <td>{strength.GBP}</td>
                                <td>{strength.CHF}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default StrengthsList;
