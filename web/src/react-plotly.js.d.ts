declare module 'react-plotly.js' {
    import * as React from 'react';
    import { PlotParams } from 'plotly.js';
  
    export interface PlotlyRenderProps extends PlotParams {
      debug?: boolean;
      data: Partial<Plotly.PlotData>[];
      layout: Partial<Plotly.Layout>;
      frames?: Partial<Plotly.Frame>[];
      revision?: number;
      onInitialized?: (figure: Readonly<PlotParams>, graphDiv: HTMLElement) => void;
      onUpdate?: (figure: Readonly<PlotParams>, graphDiv: HTMLElement) => void;
      onPurge?: (figure: Readonly<PlotParams>, graphDiv: HTMLElement) => void;
      onError?: (error: Error) => void;
      onAfterExport?: () => void;
      onClick?: (event: Readonly<Plotly.PlotMouseEvent>) => void;
      onBeforeHover?: (event: Readonly<Plotly.PlotMouseEvent>) => boolean;
      onHover?: (event: Readonly<Plotly.PlotMouseEvent>) => void;
      onUnhover?: (event: Readonly<Plotly.PlotMouseEvent>) => void;
      onSelected?: (event: Readonly<Plotly.PlotSelectionEvent>) => void;
      onDeselect?: (event: Readonly<Plotly.PlotSelectionEvent>) => void;
    }
  
    const Plot: React.FC<Partial<PlotlyRenderProps>>;
  
    export default Plot;
  }
  