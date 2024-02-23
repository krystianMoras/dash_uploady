import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { Uploady, useBatchAddListener } from '@rpldy/uploady';
import { useBatchFinalizeListener, useItemFinalizeListener, useItemErrorListener } from "@rpldy/uploady";
import { useState } from 'react';
import { set } from 'ramda';

const BatchListener = ({ setProps }) => {
    const [totalFiles, setTotalFiles] = useState(0);
    const [progress, setProgress] = useState(0);
    const [errors, setErrors] = useState([]);

    useBatchAddListener((batch) => {
        setTotalFiles(batch.items.length);
        setProgress(0);
        if (setProps) {
            setProps({ finished: false, errors: [], progress: 0 });
        }
    });

    useBatchFinalizeListener(() => {
        if (setProps) {
            setProps({ finished: true, progress: progress / totalFiles, errors: errors });
        }
    });

    useItemFinalizeListener((item) => {

        if (setProps) {
            setProgress(prevProgress => prevProgress + 1);
            if (item.state !== "finished") {
                setErrors(prevErrors => [...prevErrors, item.file.name]);
                setProps({ errors: errors, progress: progress / totalFiles });
            }
            else {
                setProps({ progress: progress / totalFiles });
            }
        }
    });

    return null;
};

const DashUploadyBuild = (props) => {

    return (
        <Uploady
            multiple={props.multiple}
            webkitdirectory={props.webkitdirectory}
            destination={{ url: props.destination_url }}
        >
            <BatchListener setProps={props.setProps} />
            {props.children}
        </Uploady>
    );
};


DashUploadyBuild.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Children of DashUploady
     */
    children: PropTypes.node,

    multiple: PropTypes.bool,
    progress: PropTypes.number,

    webkitdirectory: PropTypes.bool,

    finished: PropTypes.bool,
    errors: PropTypes.array,
    destination_url: PropTypes.string

};
DashUploadyBuild.defaultProps = {
    multiple: false,
    webkitdirectory: false,
    finished: true,
    progress: 0,
    errors: [],
};

export default DashUploadyBuild;